hello_name: main.o func.o
	g++ main.o func.o -o hello_name
main.o: main.cpp
	g++ -c main.cpp
func.o: func.cpp
	g++ -c func.cpp

clean:
	rm *.o hello_name
