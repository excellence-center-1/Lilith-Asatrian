#include <iostream>
#include <memory>
#include <unordered_map>

class Shape
{
public:
    virtual void draw() const = 0;
    virtual std::unique_ptr<Shape> clone() const = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape
{
public:
    void draw() const override
    {
        std::cout << "Circle" << std::endl;
    }

    std::unique_ptr<Shape> clone() const override
    {
        return std::unique_ptr<Shape>(new Circle(*this));
    }
};

class Square : public Shape
{
public:
    void draw() const override
    {
        std::cout << "Square" << std::endl;
    }

    std::unique_ptr<Shape> clone() const override
    {
        return std::unique_ptr<Shape>(new Square(*this));
    }
};

class Triangle : public Shape
{
public:
    void draw() const override
    {
        std::cout << "Triangle" << std::endl;
    }

    std::unique_ptr<Shape> clone() const override
    {
        return std::unique_ptr<Shape>(new Triangle(*this));

    }
};

class ShapeFactory {
    private:
    std::unordered_map<std::string, std::unique_ptr<Shape>> prototype;
    public:
    ShapeFactory() {
        prototype["Circle"] = std::unique_ptr<Shape>(new Circle());   
        prototype["Square"] = std::unique_ptr<Shape>(new Square());   
        prototype["Triangle"] = std::unique_ptr<Shape>(new Triangle());    
    }

    std::unique_ptr<Shape> createShape(const std::string &type)
{
    for (const std::pair<const std::string, std::unique_ptr<Shape>> &entry : prototype)
    {
        if (entry.first == type)
            return entry.second->clone();
    }
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