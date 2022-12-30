#include <iostream>
#include <vector>
#include <gl/glut.h>
#include <cmath>
#include <math.h>
#define _USE_MATH_DEFINES
# define M_PIl 3.141592653589793238462643383279502884L /* pi */
using namespace std;

class xPoint3D
{
public:
    float x, y, z;
    xPoint3D()
    {
        x = y = z = 0;
    };
};

enum AxisStandard
{
    None,
    XAxis,
    YAxis
};

GLsizei winWidth = 1000, winHeight = 600; 
vector<xPoint3D> arInputPoint; 
vector<vector<xPoint3D>> arRotPoint; 
float fRotate = 360; 
AxisStandard curAXIS = None; 

void init() 
{
    glClearColor(0.f, 0.f, 0.f, 1.f);               //background color
    glMatrixMode(GL_PROJECTION);
}

void mydisplay()  
{
    glClear(GL_COLOR_BUFFER_BIT);
    
    //X-axis
    curAXIS == XAxis? glColor3f(0.f, 1.f, 0.f): glColor3f(1.f, 1.f, 1.f);
    glBegin(GL_LINE_LOOP); //연결된 선분을 그리기 위함
    glVertex3f(-winWidth, 0, 0.0); //시작점
    glVertex3f(winWidth, 0, 0.0); //끝점
    glEnd();
    
    //Y-axis
    curAXIS == YAxis ? glColor3f(0.f, 1.f, 0.f) : glColor3f(1.f, 1.f, 1.f);
    glBegin(GL_LINE_LOOP);
    glVertex3f(0, -winHeight, 0.0); //시작점
    glVertex3f(0, winHeight, 0.0); //끝점
    glEnd();
    
    //Input point
    glPointSize(5.0);  // 그려지는 점의 크기 지ㅇ
    glColor3f(1, 0, 0); //컬러 지정
    glBegin(GL_POINTS);
    for (int i = 0; i < arInputPoint.size(); i++) 
    {
        glVertex3f(arInputPoint[i].x, arInputPoint[i].y, arInputPoint[i].z);
    }
    glEnd(); 

    //Rotate point
    glPointSize(5.0);  // 그려지는 점의 크기
    glColor3f(1, 0, 0); //컬러 지정
    glBegin(GL_POINTS); 
    for (int i = 0; i < arRotPoint.size(); i++)
    {
        for (int j = 0; j < arRotPoint[i].size(); j++)
        {
            glVertex3f(arRotPoint[i][j].x, arRotPoint[i][j].y, 0);
        }
    }
    glEnd();
    
    glFlush();
}


void MyMouseClick(GLint Button, GLint state, GLint X, GLint Y) 
{
    if (Button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) 
    {
        xPoint3D temp;
        
        temp.x = -(winWidth / 2 - X); 
        temp.y = winHeight / 2 - Y;
        temp.z = 0; 
        arInputPoint.push_back(temp);
        glutPostRedisplay(); 
    }
}
void winReshapeFcn(int newWidth, int newHeight) 
{
    /*  Reset viewport and projection parameters  */
    glViewport(0, 0, newWidth, newHeight); 
    glMatrixMode(GL_PROJECTION); 
    glLoadIdentity(); 
    glOrtho(-GLdouble(newWidth)/2, GLdouble(newWidth)/2, -GLdouble(newHeight)/2, GLdouble(newHeight)/2, -1.0, 1.0);

    /*  Reset display-window size parameters.  */
    winWidth = newWidth; 
    winHeight = newHeight; 

    glMatrixMode(GL_MODELVIEW);
}

void MyMainMenu(int entryID)
{
    if (entryID == 1)
        curAXIS = XAxis;
    else if (entryID == 2)
        curAXIS = YAxis;
    else if (entryID == 3)
    {
        curAXIS = None;
        arInputPoint.clear();
        for (int i = 0; i < arRotPoint.size(); i++)
            arRotPoint[i].clear();
        arRotPoint.clear();
    }
    else if (entryID == 4)
        exit(0);
    glutPostRedisplay(); 
}

void saveRotPoint()
{
    int iCircle = 360;
    float fCurRotate = 0;

    for (int i = 0; i < (iCircle / fRotate) - 1; i++)
   {
      fCurRotate += fRotate; 
      float fRadian = fCurRotate * (M_PIl / 180.0);

      vector<xPoint3D> tempAry;
      xPoint3D tempPt;


      for (int j = 0; j < arInputPoint.size(); j++)
      {
         if (curAXIS == XAxis) 
         {
            tempPt.x = arInputPoint[j].x;
            tempPt.y = arInputPoint[j].y * cos(fRadian) - arInputPoint[j].z * sin(fRadian);
            tempPt.z = arInputPoint[j].y * sin(fRadian) + arInputPoint[j].z * cos(fRadian);
            tempAry.push_back(tempPt);

         }
         else if (curAXIS = YAxis) 
         {
            tempPt.x = arInputPoint[j].z * sin(fRadian) + arInputPoint[j].x * cos(fRadian);
            tempPt.y = arInputPoint[j].y;
            tempPt.z = arInputPoint[j].z * cos(fRadian) - (arInputPoint[j].x) * sin(fRadian);
            tempAry.push_back(tempPt);
         }
      }

      arRotPoint.push_back(tempAry); 
   }
}

void MySubMenu(int entryID)
{
    if (entryID == 1)       fRotate = 20;
    else if (entryID == 2)  fRotate = 30;
    else if (entryID == 3)  fRotate = 45;
    else if (entryID == 4)  fRotate = 60;
    else if (entryID == 5)  fRotate = 90;
    else if (entryID == 6)  fRotate = 180; 

    saveRotPoint(); 
    glutPostRedisplay(); 
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv); 
    glutInitDisplayMode(GLUT_RGB); 
    glutInitWindowSize(winWidth, winHeight); 
    glutInitWindowPosition(300, 50);
    glutCreateWindow("YIHYUN_CG");
    
    init();

    GLint MySubMenuID = glutCreateMenu(MySubMenu);
    glutAddMenuEntry("20", 1);
    glutAddMenuEntry("30", 2);
    glutAddMenuEntry("45", 3);
    glutAddMenuEntry("60", 4);
    glutAddMenuEntry("90", 5);
    glutAddMenuEntry("180", 6); 

    GLint MyMainMenuID = glutCreateMenu(MyMainMenu);
    glutAddMenuEntry("X Axis", 1);
    glutAddMenuEntry("Y Axis", 2);
    glutAddSubMenu("Rotate Angle", MySubMenuID);
    glutAddMenuEntry("Clear", 3);
    glutAddMenuEntry("Exit", 4); 

    glutAttachMenu(GLUT_RIGHT_BUTTON); 
    
    glutDisplayFunc(mydisplay); 
    glutReshapeFunc(winReshapeFcn); 
    glutMouseFunc(MyMouseClick);
    glutMainLoop();

    return 0;
}

