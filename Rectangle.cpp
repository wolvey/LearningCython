#include "Rectangle.h"

using namespace shapes;

Rectangle::Rectangle(int x0 ,int y0, int x1, int y1) :
  x0(x0), y0(y0), x1(x1), y1(y1)
{
}

Rectangle::~Rectangle() {
}

int Rectangle::getLength() {
  return x1 - x0;
}

int Rectangle::getHeight() {
  return y1 - y0;
}

int Rectangle::getArea() {
  return getLength() * getHeight();
}

void Rectangle::move(int dx, int dy) {
  x0 += dx;
  y0 += dy;
  x1 += dx;
  y1 += dy;
}
