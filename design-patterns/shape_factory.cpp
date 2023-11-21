// Main function to test the ShapeFactory
#include <iostream>
#include <memory>

class Shape
{
public:
    virtual void draw() const = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape
{
public:
    void draw() const override
    {
        std::cout << "Circle" << std::endl;
    }
};

class Square : public Shape
{
public:
    void draw() const override
    {
        std::cout << "Square" << std::endl;
    }
};

class Triangle : public Shape
{
public:
    void draw() const override
    {
        std::cout << "Triangle" << std::endl;
    }
};

class ShapeFactory
{
public:
    std::unique_ptr<Shape> createShape(const std::string &type)
    {
        if (type == "Circle")
            return std::unique_ptr<Shape>(new Circle());
        else if (type == "Square")
            return std::unique_ptr<Shape>(new Square());
        else if (type == "Triangle")
            return std::unique_ptr<Shape>(new Triangle());
        else
            return nullptr;
    }
};

int main()
{
    ShapeFactory shapeFactory;

    // Test cases
    std::unique_ptr<Shape> circle = shapeFactory.createShape("Circle");
    if (circle)
        circle->draw();

    std::unique_ptr<Shape> square = shapeFactory.createShape("Square");
    if (square)
        square->draw();

    std::unique_ptr<Shape> triangle = shapeFactory.createShape("Triangle");
    if (triangle)
        triangle->draw();

    std::unique_ptr<Shape> unknownShape = shapeFactory.createShape("Rectangle");
    if (!unknownShape)
    {
        std::cout << "Unknown shape requested\n";
    }

    return 0;
}