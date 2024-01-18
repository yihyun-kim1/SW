#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <math.h>
#include <iostream>
#ifdef __APPLE_CC__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#define WIRE 0
#define SHADE 1

#define PI 3.141592
#define R 10

using namespace std;

static bool spinning = true;
static GLfloat currentAngleOfRotation = 0.0;
//이거 다 큐브 회전, examples 북마크에서 spinning square 코드 참고!

typedef struct {
    float x;
    float y;
    float z;
} Point;

typedef struct {
    unsigned int ip[3];
} Face;

int pnum;
int fnum;

Point* mpoint = NULL; Face* mface = NULL;

GLfloat angle = 0; /* in degrees */

int moving;
int mousebegin;
int light_moving;

int scaling = 0;
int status = 0; // WIRE or SHADE

// Colors
GLfloat WHITE[] = { 1, 1, 1 };
GLfloat RED[] = { 1, 0, 0 };
GLfloat GREEN[] = { 0, 1, 0 };
GLfloat MAGENTA[] = { 1, 0, 1 };
GLfloat Lemon[] = { 1, 0.9, 0.6 };
GLfloat CYAN[] = { 0, 1, 1 };
GLfloat lightCYAN[] = { 0.8, 1, 1 };

class Camera {
    double theta;      // x, z 위치
    double y;          // 현재의 y 위치
    double dTheta;     // 카메라 - 여러 방향으로 움직이기 위한 조절
    double dy;         // 카메라 - 상하 조절을 위한 조절
public:
    Camera() : theta(0), y(3), dTheta(0.04), dy(0.2) {}
    double getX() { return 10 * cos(theta); }
    double getY() { return y; }
    double getZ() { return 10 * sin(theta); }
    void moveRight() { theta += dTheta; } //카메라 우로 이동
    void moveLeft() { theta -= dTheta; } //카메라 좌로 이동
    void moveUp() { y += dy; } //카메라 높이 조절 - 상향
    void moveDown() { if (y > dy) y -= dy; } //카메라 높이 조절 - 하향
};

class Ball {
    double radius;
    GLfloat* color;
    double maximumHeight;
    double x;
    double y;
    double z;
    int direction;

public:
    Ball(double r, GLfloat* c, double h, double x, double z) :
        radius(r), color(c), maximumHeight(h), direction(-1),
        y(h), x(x), z(z) {
    }
    void update() {
        y += direction * 0.05;
        if (y > maximumHeight) {
            y = maximumHeight; direction = -1;
        }
        else if (y < radius) {
            y = radius; direction = 1;
        }
        glPushMatrix();
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, color);
        glTranslated(x, y, z);
        glutSolidSphere(radius, 30, 30);
        glPopMatrix();
    }
};

// A checkerboard class.  A checkerboard has alternating red and white
// squares.  The number of squares is set in the constructor.  Each square
// is 1 x 1.  One corner of the board is (0, 0) and the board stretches out
// along positive x and positive z.  It rests on the xz plane.  I put a
// spotlight at (4, 3, 7).
// 바닥 만드는 클래스 구현
class CheckFloor {
    int displayListId;
    int width;
    int depth;
public:
    CheckFloor(int width, int depth) : width(width), depth(depth) {}
    double centerx() { return width / 2; }
    double centerz() { return depth / 2; }
    void create() {
        displayListId = glGenLists(1);
        glNewList(displayListId, GL_COMPILE);
        GLfloat lightPosition[] = { 4, 3, 7, 1 };
        glLightfv(GL_LIGHT0, GL_POSITION, lightPosition);
        glBegin(GL_QUADS);
        glNormal3d(0, 1, 0);
        for (int x = 0; x < width - 1; x++) {
            for (int z = 0; z < depth - 1; z++) {
                glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE,
                    (x + z) % 2 == 0 ? RED : WHITE);
                glVertex3d(x, 0, z);
                glVertex3d(x + 1, 0, z);
                glVertex3d(x + 1, 0, z + 1);
                glVertex3d(x, 0, z + 1);
            }
        }
        glEnd();
        glEndList();
    }


    void draw() {
        glCallList(displayListId);
    }
};

//카메라, 바닥, 공 -> 글로벌 변수로 선언
CheckFloor checkfloor(8, 8);
Camera camera;
Ball balls[] = {
  Ball(1, GREEN, 7, 6, 1),
  Ball(1.5, MAGENTA, 6, 3, 4),
  Ball(0.4, WHITE, 5, 1, 7)
};


// Application-specific initialization: Set up global lighting parameters
// and create display lists.
void init() {
    glEnable(GL_DEPTH_TEST);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, WHITE);
    glLightfv(GL_LIGHT0, GL_SPECULAR, WHITE);
    glMaterialfv(GL_FRONT, GL_SPECULAR, WHITE);
    glMaterialf(GL_FRONT, GL_SHININESS, 30);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    checkfloor.create();
}

void MakeGL_Model(void)
{
    int i;

    //  if (glIsList(1)) glDeleteLists(1, 1);
    //  glNewList(1, GL_COMPILE); glPushMatrix();
        //있으면 바닥이랑 호환 X

    glRotatef(angle, 0.0, 1.0, 0.0);
    glScalef(0.01, 0.01, 0.01);
    //원래 각 값 scalefactor임

    for (i = 0; i < fnum; i++) {
        glBegin(GL_TRIANGLES);
        glVertex3f(mpoint[mface[i].ip[0]].x,
            mpoint[mface[i].ip[0]].y, mpoint[mface[i].ip[0]].z);
        glVertex3f(mpoint[mface[i].ip[1]].x,
            mpoint[mface[i].ip[1]].y, mpoint[mface[i].ip[1]].z);
        glVertex3f(mpoint[mface[i].ip[2]].x,
            mpoint[mface[i].ip[2]].y, mpoint[mface[i].ip[2]].z);
        glEnd();
    }
    glPopMatrix();
    glEndList();
}

void mouse(int button, int state, int x, int y) {
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
        glEnable(GL_CULL_FACE); glCullFace(GL_FRONT); glFrontFace(GL_CW);
        //glcullface -> gl_back으로 하면 전면이 제거됨 (GL은 반시계방향으로 그려진걸 전면으로하기때문) 따라서 FRONT로 수정!
    } //왼쪽 마우스 버튼 누르면 backface culling 켜지게
    if (button == GLUT_LEFT_BUTTON && state == GLUT_UP) {
        glDisable(GL_CULL_FACE);
    } //버튼 떼면 backface culling 꺼지게
    if ((button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)) {
        //오른쪽 버튼 누르면 FLAT shading
        glShadeModel(GL_FLAT);
    }
    if ((button == GLUT_RIGHT_BUTTON && state == GLUT_UP)) {
        //버튼 안 누르거나 오른쪽 버튼 떼면 SMOOTH shading
        glShadeModel(GL_SMOOTH);
    }
}

// Draws one frame, the checkerboard then the balls, from the current camera
// position.
void display(void) {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    if (status == WIRE)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
    else if (status == SHADE)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
    //  else if (status == F)
    //      glFrustum(-1.0f, 1.0f, -1.0f, 1.0, 1.0f, 20.0f);

    glLoadIdentity();
    gluLookAt(camera.getX(), camera.getY(), camera.getZ(),
        checkfloor.centerx(), 0.0, checkfloor.centerz(),
        0.0, 1.0, 0.0);
    checkfloor.draw();
    for (int i = 0; i < sizeof balls / sizeof(Ball); i++) {
        balls[i].update();
    }
    // Make a torus floating 0.5 above the x-z plane.  The standard torus in
    // the GLUT library is, perhaps surprisingly, a stack of circles which
    // encircle the z-axis, so we need to rotate it 90 degrees about x to
    // get it the way we want.
    glPushMatrix();
    glTranslatef(5, 1, 5);
    glRotatef(90.0, 1.0, 0.0, 0.0);
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, lightCYAN);
    glutSolidTorus(0.275, 0.5, 16, 40);
    glPopMatrix();

    // Make a cone.  The standard cone "points" along z; we want it pointing
    // along y, hence the 270 degree rotation about x.
    glPushMatrix();
    glTranslatef(5, 0, 5);
    glRotatef(270.0, 1.0, 0.0, 0.0);
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, CYAN);
    glutSolidCone(1.0, 2.0, 70, 12);

    //Make Square and 회전시키기
    glPushMatrix();
    glTranslatef(-2, 3, 1);
    glRotatef(currentAngleOfRotation, 0.0, 0.0, 1.0);
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, Lemon);
    glutSolidCube(1.2);
    //solid인데 왜 꽉 안차지? 찬건가
    glPopMatrix();
    MakeGL_Model(); // 왜 이 줄만 있으면 바닥이랑 호환이 안되지?

    glFlush();
    glutSwapBuffers();
}

// On reshape, constructs a camera that perfectly fits the window.
void reshape(GLint w, GLint h) {
    glViewport(0, 0, w, h);
    GLfloat aspect = (GLfloat)w / (GLfloat)h;
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(40.0, GLfloat(w) / GLfloat(h), 1.0, 150.0);
    //glFrustum(-1.0f, 1.0f, -1.0f, 1.0, 1.0f, 20.0f);
    glMatrixMode(GL_MODELVIEW);
}

// Requests to draw the next frame.
void timer(int v) {
    glutPostRedisplay(); //윈도우를 다시 그림
    glutTimerFunc(1000 / 60, timer, v); //다음 타이머 이벤트는 1000/60ms 후 호출됨

    if (spinning) {
        currentAngleOfRotation += 1.0;
        if (currentAngleOfRotation > 360.0) {
            currentAngleOfRotation -= 360.0;
        } //큐브 회전하는 코드 !

        glutPostRedisplay();
    }
}

// Moves the camera according to the key pressed, then ask to refresh the
// display.
void special(int key, int, int) {
    printf("key %d\n", key);
    switch (key) {
    case GLUT_KEY_LEFT: camera.moveLeft(); break;
    case GLUT_KEY_RIGHT: camera.moveRight(); break;
    case GLUT_KEY_UP: camera.moveUp(); break;
    case GLUT_KEY_DOWN: camera.moveDown(); break;
    }
    glutPostRedisplay();
}

void normalKey(unsigned char key, int x, int y)
{
    printf("key %d\n", key);
    switch (key) {
    case 'w':
        status = WIRE;  glutPostRedisplay(); break;
    case 's':
        status = SHADE; glutPostRedisplay(); break;
    }

    glutPostRedisplay();
}


int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowPosition(80, 80);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Yihyun_CG_Final");
    glutDisplayFunc(display);
    glutMouseFunc(mouse);
    glutKeyboardFunc(normalKey);
    glutReshapeFunc(reshape);
    glutSpecialFunc(special);
    glutTimerFunc(100, timer, 0);
    init();
    glutMainLoop();

    return 0;
}
