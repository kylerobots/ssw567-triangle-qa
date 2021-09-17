# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(1.5, 1.5, 1.5),
                         'Equilateral', '1.5,1.5,1.5 should be equilateral')

    def testEquilateralTrianglesC(self):
        self.assertEqual(classifyTriangle(100000.0, 100000.0, 100000.0),
                         'Equilateral', '100000.0,100000.0,100000.0 should be equilateral')

    def testIsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(2.8, 2.8, 1.0),
                         'Isosceles', '2.8,2.8,1.0 should be isosceles')

    def testIsoscelesTrianglesB(self):
        self.assertEqual(classifyTriangle(1.5, 1000.0, 1000.0),
                         'Isosceles', '1.5,1000.0,1000.0 should be isosceles')

    def testIsoscelesTrianglesC(self):
        self.assertEqual(classifyTriangle(7.6, 1000.0, 1000.0),
                         'Isosceles', '1.5,1000.0,1000.0 should be isosceles')

    def testNotTrianglesA(self):
        self.assertEqual(classifyTriangle(0.0, 0.0, 0.0),
                         'NotATriangle', '0.0,0.0,0.0 should not be a triangle')

    def testNotTrianglesB(self):
        self.assertEqual(classifyTriangle('0.0', 0.0, 0.0),
                         'NotATriangle', '"0.0",0.0,0.0 should not be a triangle')

    def testNotTrianglesC(self):
        self.assertEqual(classifyTriangle(-2.0, 2.0, 1.0),
                         'NotATriangle', '-2.0,2.0,1.0 should not be a triangle')

    def testNotTrianglesD(self):
        self.assertEqual(classifyTriangle(1.0, 2.0, 3.0),
                         'NotATriangle', '1.0,2.0,3.0 should not be a triangle')

    def testNotTrianglesE(self):
        self.assertEqual(classifyTriangle(0.5, 0.5, 2.0),
                         'NotATriangle', '0.5,0.5,2.0 should not be a triangle')

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right',
                         '5,3,4 is a Right triangle')

    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(1.0, 2.0, 2.5),
                         'Scalene', '1.0,2.0,2.5 should be scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
