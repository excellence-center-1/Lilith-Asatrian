SRC = src
OBJ = obj
INCLUDE = include
SOURCES = $(wildcard $(SRC)/*.cpp)
OBJECTS = $(SOURCES:$(SRC)/%.cpp=$(OBJ)/%.o)
EXECUTABLE = calc
CXX = g++
CXXFLAGS = -I$(INCLUDE)

all: $(OBJ) $(EXECUTABLE) 

$(EXECUTABLE): $(OBJECTS)
	$(CXX) $(OBJECTS) -o $(EXECUTABLE)

$(OBJ)/%.o: $(SRC)/%.cpp $(INCLUDE)/%.h 
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(OBJ)/%.o: $(SRC)/%.cpp 
	$(CXX) -c $< -o $@

$(OBJ):
	mkdir -p $(OBJ)

.PHONY: clean
clean:
	rm -rf $(OBJ) $(EXECUTABLE)
