.PHONY: all
all: rect.so
	python rectangle_test.py

rect.so: rect.pyx Rectangle.cpp Rectangle.h setup.py
	python setup.py build_ext --inplace

.PHONY: clean
clean:
	rm -fr rect.so rect.cpp build
