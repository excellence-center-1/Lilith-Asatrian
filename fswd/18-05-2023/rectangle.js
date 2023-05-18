class Rectangle {
  #width;
  #height;
  constructor(width, height) {
    this.#height = height;
    this.#width = width;
  } 

  //getters for accessing height and width
  get width() {
    return this.#width;
  }
  get height() {
    return this.#height;
  }

  //setters for setting new values
  set width(newWidth) {
    if(newWidth <= 0 || isNaN(newWidth)){
    console.error("Invalid width value."); 
  }
  else{
    this.#width = newWidth;
  }
}
  set height(newHeight) {
    if(newHeight <= 0 || isNaN(newHeight)){
      console.error("Invalid height value."); 
    }
    else{
      this.#height = newHeight;
    }
  }
  
  //calculate area
  calcArea() {
    return this.#height * this.#width;
  }
  get area() {
    return this.calcArea();
  }
  //calculate perimeter
  calcPerimeter() {
    return (this.#height + this.#width) * 2;
  }
  get perimeter() {
    return this.calcPerimeter();
  } 
}
// Create an instance of Rectangle
const rectangle = new Rectangle(5, 10);

// Display the area and perimeter
console.log('Area:', rectangle.area);
console.log('Perimeter:', rectangle.perimeter);

// Update the width and height using the setter methods
rectangle.width = 8;
rectangle.height = 15;

// Display the updated area and perimeter
console.log('Updated Area:', rectangle.area);
console.log('Updated Perimeter:', rectangle.perimeter);

// Try setting invalid values
rectangle.width = -2; 
rectangle.height = 0;