#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <thread>
#include <chrono>

/// <summary>
/// Получить содержимое файла
/// </summary>
/// <param name="filename">Имя считываемого файла</param>
/// <returns>Содержимое файла</returns>
std::string getFileContent(std::string filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cout << "Error open file";
        return "";
    }

    std::string content(
        (std::istreambuf_iterator<char>(file)),
        std::istreambuf_iterator<char>());
    file.close();
    return content;
}

/// <summary>
/// Функция разделения строки по разделителю
/// </summary>
/// <param name="content">Исходная строка</param>
/// <param name="delimeter">Разделитель</param>
/// <returns>Список подстрок</returns>
std::vector<std::string> split(
    std::string content, 
    std::string delimeter) {

    std::vector<std::string> parts;
    int start = 0;
    int end = content.find(delimeter);

    while (end != std::string::npos) {
        parts.push_back(content.substr(start,end-start));
        start = end + delimeter.length();
        end = content.find(delimeter, start);
    }
    parts.push_back(content.substr(start));
    return parts;
}

int main()
{
    std::string filename = "animation.txt";
    std::string content = getFileContent(filename);
    std::vector<std::string> frames = 
                        split(content,"FRAME");

    while(true)
    {
        for (std::string frame : frames)
        {
            system("cls");
            std::cout << frame << std::endl;

            std::this_thread::sleep_for
            (std::chrono::milliseconds(33));
        }
    }
}
