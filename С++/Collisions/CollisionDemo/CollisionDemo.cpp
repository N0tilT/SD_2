﻿#include <iostream>
#include "raylib.h"
#include "raymath.h"
#include <vector>

const int MAX_WIDTH = 800;
const int MAX_HEIGHT = 600;
const float damping = -0.05f;

struct Circle {
    Vector2 position;
    Vector2 velocity;
    Vector2 accelerate;
    float radius;
    float weight;
};

int GenerateCircles(std::vector<Circle>& circles, int count = 10,int minRadius = 30,int maxRadius = 60,
    int minVelocity=0,int maxVelocity =0) {
    for (int i = 0; i < count; i++)
    {
        Vector2 velocity = {
           GetRandomValue(minVelocity,maxVelocity),
           GetRandomValue(minVelocity,maxVelocity)
        };
        Vector2 accelerate = { 0,0 };
        float radius = GetRandomValue(minRadius, maxRadius);
        float weight = radius / 3;
        Vector2 position = {
            GetRandomValue(0 + radius,MAX_WIDTH - radius),
            GetRandomValue(0 + radius,MAX_HEIGHT - radius)
        };
        circles.push_back(Circle{ position,velocity,accelerate,radius,weight });
    }
    return count;
}

void StaticCollisionResolution(Circle& a, Circle& b) {
    Vector2 delta = {
        b.position.x - a.position.x,
        b.position.y - a.position.y
    };
    float distance = Vector2Length(delta);
    float overlap = distance - a.radius - b.radius;
    Vector2 direction = Vector2Scale(Vector2Normalize(delta), overlap / 2.0);
    a.position = Vector2Add(a.position, direction);
    b.position = Vector2Add(b.position, Vector2Negate(direction));
}

void DynamicCollisionResolution(Circle& a, Circle& b) {
    Vector2 first = a.position;
    Vector2 second = b.position;
    //оси столкновения - нормаль и касательная
    Vector2 dir = Vector2Subtract(second, first);
    Vector2 normal = Vector2Normalize(dir);
    Vector2 tangent = { -normal.y,normal.x };
    //Проекции на оси столкновения
    float dpNormA = Vector2DotProduct(a.velocity, normal);
    float dpNormB = Vector2DotProduct(b.velocity, normal);
    float dpTangA = Vector2DotProduct(a.velocity, tangent);
    float dpTangB = Vector2DotProduct(b.velocity, tangent);
    //Сохранение импульса в 1мерном пространстве
    float p1 = (dpNormA * (a.weight - b.weight) + 2 * b.weight * dpNormB) / (a.weight + b.weight);
    float p2 = (dpNormB * (b.weight - a.weight) + 2 * a.weight * dpNormA) / (a.weight + b.weight);
    //Применяем измененный импульс к скоростям кругов
    a.velocity = Vector2Add(Vector2Scale(tangent, dpTangA), Vector2Scale(normal, p1));
    b.velocity = Vector2Add(Vector2Scale(tangent, dpTangB), Vector2Scale(normal, p2));
}

void HandleCollision(std::vector<std::pair<Circle*,Circle*>>& collisions, Circle& a, Circle& b) {
    Vector2 delta = { b.position.x - a.position.x,b.position.y - a.position.y, };
    float distance = Vector2Length(delta);
    float minDistance = a.radius + b.radius;
    if (distance < minDistance) {
        StaticCollisionResolution(a, b);
        Circle* pa = &a;
        Circle* pb = &b;
        collisions.push_back({ pa,pb });
    }
}

int main()
{
    InitWindow(MAX_WIDTH, MAX_HEIGHT,"Bounce");
    SetTargetFPS(60);

    bool dragging = false;
    Circle* selectedCircle = nullptr;

    std::vector<Circle> circles;
    GenerateCircles(circles, 5, 10, 20, 0, 0);

    while (!WindowShouldClose()) {
        Vector2 mousePosition = GetMousePosition();
        
        if (IsMouseButtonPressed(MOUSE_BUTTON_LEFT)) {
            for (auto& circle : circles) {
                if (CheckCollisionPointCircle(mousePosition, circle.position, circle.radius)) {
                    dragging = true;
                    selectedCircle = &circle;
                    break;
                }
            }
        }

        //if(selectedCircle!=nullptr)
        //    selectedCircle->position = mousePosition;

        std::vector<std::pair<Circle*, Circle*>> collisions;

        for (int i = 0; i<circles.size()-1; ++i) {
            for (int j = i + 1; j < circles.size(); ++j) {
                HandleCollision(collisions, circles[i], circles[j]);
            }
        }

        for (auto& collision : collisions) {
            DynamicCollisionResolution(*collision.first, *collision.second);
        }

        if (IsMouseButtonReleased(MOUSE_BUTTON_LEFT)) {
            if (selectedCircle != nullptr) {
                Vector2 direction = Vector2Subtract(mousePosition, selectedCircle->position);
                float distance = Vector2Length(direction);
                Vector2 acceleration = Vector2Negate(Vector2Scale(Vector2Normalize(direction), distance * 0.1f));
                selectedCircle->velocity = acceleration;
            }
            dragging = false;
            selectedCircle = nullptr;
        }

        for (auto& circle : circles) {
            circle.accelerate = Vector2Scale(circle.velocity, damping);
            circle.velocity = Vector2Add(circle.velocity, circle.accelerate);
            circle.position = Vector2Add(circle.position,circle.velocity);
        }

        BeginDrawing();
        ClearBackground(RAYWHITE);
        //for circle in circles
        for (const auto& circle : circles) { 
            DrawCircleV(circle.position, circle.radius, BLUE);
        }
        EndDrawing();
    }
}
