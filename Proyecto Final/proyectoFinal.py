from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame

w,h,z= 600,600,600
giroEnX = 0
giroEnY = 0
giroEnZ = 0

morado = os.path.dirname(__file__)+"\morado.jpg"
blanco = os.path.dirname(__file__)+"\white.jpg"
rojo = os.path.dirname(__file__)+"\guinda.jpg"
celeste = os.path.dirname(__file__)+"\celeste.jpg"
gris = os.path.dirname(__file__)+"\pared_piedra.jpg"
crema = os.path.dirname(__file__)+"\crema.jpg"
cafe = os.path.dirname(__file__)+"\ladrillo.jpg"
naranja = os.path.dirname(__file__)+"\orange.jpg"
amarillo = os.path.dirname(__file__)+"\yellow.jpg"
pisoCasa = os.path.dirname(__file__)+"\piso_madera.jpg"
pisoCocina = os.path.dirname(__file__)+"\piso_cocina.jpg"

def processSpecialKeys(key, x, y):
    global giroEnX,giroEnY,giroEnZ

    if key == GLUT_KEY_RIGHT:
        giroEnY = giroEnY-30
    if key == GLUT_KEY_LEFT:
        giroEnY = giroEnY+30
    if key == GLUT_KEY_DOWN:
        giroEnX = giroEnX-30
    if key == GLUT_KEY_UP:
        giroEnX = giroEnX+30
    if key == GLUT_KEY_F1:
        giroEnZ = giroEnZ+30
    if key == GLUT_KEY_F2:
        giroEnZ = giroEnZ-30

def loadTexture(cadena):
    textureSurface = pygame.image.load(cadena)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
    0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

def pared(x0,y0,x1,y1,z0,z1,text1,text2):
    g=5 #grueso de la pared
    a = z1 #altura pared
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    
    if (x0==x1):
        loadTexture(text1)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(x0+g,z0,-y0)
        glTexCoord2f(0, 2)
        glVertex3f(x0+g,z0,-y1)
        glTexCoord2f(2, 2)
        glVertex3f(x0+g,z1,-y1)
        glTexCoord2f(2, 0)
        glVertex3f(x0+g,z1,-y0)
        glEnd()

        loadTexture(text2)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(x0-g,z0,-y0)
        glTexCoord2f(0, 2)
        glVertex3f(x0-g,z0,-y1)
        glTexCoord2f(2, 2)
        glVertex3f(x0-g,z1,-y1)
        glTexCoord2f(2, 0)
        glVertex3f(x0-g,z1,-y0)
        glEnd()

        loadTexture(blanco)
        glBegin(GL_QUADS)
        glVertex3f(x0-g,z1,-y0)
        glVertex3f(x0-g,z1,-y1)
        glVertex3f(x0+g,z1,-y1)
        glVertex3f(x0+g,z1,-y0)

        glVertex3f(x0+g,z0,-y0)
        glVertex3f(x0-g,z0,-y0)
        glVertex3f(x0-g,z1,-y0)
        glVertex3f(x0+g,z1,-y0)
        
        glVertex3f(x0+g,z0,-y1)
        glVertex3f(x0-g,z0,-y1)
        glVertex3f(x0-g,a,-y1)
        glVertex3f(x0+g,a,-y1)
        glEnd()

    if(y0==y1):
        loadTexture(text1)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(x0,z0,-y0+g)
        glTexCoord2f(2, 0)
        glVertex3f(x1,z0,-y0+g)
        glTexCoord2f(2, 2)
        glVertex3f(x1,a,-y0+g)
        glTexCoord2f(0, 2)
        glVertex3f(x0,a,-y0+g)
        glEnd()

        loadTexture(text2)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(x0,z0,-y0-g)
        glTexCoord2f(2, 0)
        glVertex3f(x1,z0,-y0-g)
        glTexCoord2f(2, 2)
        glVertex3f(x1,a,-y0-g)
        glTexCoord2f(0, 2)
        glVertex3f(x0,a,-y0-g)
        glEnd()
        
        loadTexture(blanco)
        glBegin(GL_QUADS)
        glVertex3f(x0,a,-y0+g)
        glVertex3f(x1,a,-y0+g)
        glVertex3f(x1,a,-y0-g)
        glVertex3f(x0,a,-y0-g)

        glVertex3f(x0,z0,-y0-g)
        glVertex3f(x0,z0,-y0+g)
        glVertex3f(x0,a,-y0+g)
        glVertex3f(x0,a,-y0-g)

        glVertex3f(x1,z0,-y0-g)
        glVertex3f(x1,z0,-y0+g)
        glVertex3f(x1,a,-y0+g)
        glVertex3f(x1,a,-y0-g)
        glEnd()
        
def campo(x0,x1,y0,y1,z):
    glColor3f(189/255,236/255,182/255)
    glBegin(GL_QUADS)
    glVertex3f(x0,z,-y0)
    glVertex3f(x0,z,-y1)
    glVertex3f(x1,z,-y1)
    glVertex3f(x1,z,-y0)
    glEnd()

def ventana(x0,y0,x1,y1,z0,z1,color1,color2):
    glColor3f(1,1,1)
    pared(x0,y0,x1,y1,100,z0,color1,color2)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(131/255,181/255,221/255,0.5)
    glBegin(GL_QUADS)
    if (x0==x1):
        glVertex3f(x0,z0,-y0)
        glVertex3f(x0,z0,-y1)
        glVertex3f(x0,z1,-y1)
        glVertex3f(x0,z1,-y0)
    if(y0==y1):
        glVertex3f(x0,z0,-y0)
        glVertex3f(x1,z0,-y0)
        glVertex3f(x1,z1,-y0)
        glVertex3f(x0,z1,-y0)
    glEnd()
    glDisable(GL_BLEND)
    glColor3f(1,1,1)
    pared(x0,y0,x1,y1,z1,300,color1,color2)

def cuarto():
    pared(5,0,5,244,100,300,morado,blanco)
    pared(0,5,80,5,100,300,blanco,celeste)
    ventana(80,5,220,5,180,260,blanco,celeste)
    pared(220,5,280,5,100,300,blanco,celeste)
    pared(280,5,280,244,100,300,cafe,morado)
    pared(0,240,190,240,100,300,celeste,crema)
    pared(190,240,276,240,260,300,celeste,rojo)

def sala():
    pared(280,5,600,5,100,300,blanco,rojo)
    pared(595,5,595,80,100,300,blanco,gris)
    ventana(595,80,595,160,180,260,blanco,gris)
    pared(595,160,595,210,100,300,blanco,gris)
    ventana(595,210,595,350,180,260,blanco,gris)
    pared(595,350,595,430,100,300,blanco,gris)

def baño():
    pared(185,244,185,310,100,300,gris,crema)
    pared(185,310,185,375,260,300,gris,crema)
    pared(5,380,190,380,100,300,crema,blanco)
    pared(5,244,5,295,100,300,crema,blanco)
    ventana(5,295,5,350,225,260,crema,blanco)
    pared(5,350,5,375,100,300,crema,blanco)

def recamara():
    pared(5,375,5,595,100,300,amarillo,blanco)
    pared(0,595,100,595,100,300,blanco,blanco)
    ventana(100,595,240,595,180,260,blanco,blanco)
    pared(240,595,280,595,100,300,blanco,blanco)
    pared(280,600,280,375,100,300,gris,amarillo)
    pared(190,380,276,380,260,300,rojo,blanco)
    pared(280,595,295,595,100,300,rojo,blanco)
    pared(295,595,380,595,260,300,rojo,blanco)
    pared(380,595,395,595,100,300,rojo,blanco)

def cocina():
    pared(595,430,595,460,100,300,blanco,naranja)
    ventana(595,460,595,540,180,230,blanco,naranja)
    pared(595,540,595,595,100,300,blanco,naranja)
    pared(595,430,490,430,100,300,rojo,naranja)
    pared(490,430,410,430,260,300,rojo,naranja)
    pared(410,430,390,430,100,300,rojo,naranja)
    pared(395,595,600,595,100,300,naranja,blanco)
    pared(395,595,395,435,100,300,naranja,gris)

def piso(x0,x1,y0,y1,z,text):
    loadTexture(text)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(x0,z,-y0)
    glTexCoord2f(0, 3)
    glVertex3f(x0,z,-y1)
    glTexCoord2f(3, 3)
    glVertex3f(x1,z,-y1)
    glTexCoord2f(3, 0)
    glVertex3f(x1,z,-y0)
    glEnd()

def showScreen(): 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glLight(GL_LIGHT0, GL_POSITION,(280,50,350, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT,(0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE,(1, 1, 1, 1))
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    campo(-w*3,w*3,-h*3,h*3,99)
    glColor3f(1,1,1)
    piso(0,w,0,h,100,pisoCasa)
    piso(395,600,430,600,101,pisoCocina)
    cuarto()
    sala()
    baño()
    recamara()
    cocina()
    glDisable(GL_LIGHT0)
    glDisable(GL_LIGHTING)
    glDisable(GL_COLOR_MATERIAL)
    glutSwapBuffers()

def iterate():  
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION) #Seleccionamos la matriz de proyección
    glLoadIdentity()#Limpiamos la matriz seleccionada
    gluPerspective(45,1,30,-30)
    gluLookAt(900+giroEnX,1200+giroEnY,300+giroEnZ,w/2,h/2,-z/2,0,1,0)
    glMatrixMode (GL_MODELVIEW) #Seleccionamos la matriz del modelo 
    glLoadIdentity()#Limpiamos la matriz seleccionada, a partir de este punto lo que se haga quedara en la matriz del modelo de vista

def main():
    glutInit() # Iniciamos la instancia de glut
    glutInitDisplayMode(GLUT_RGBA) # Asignamos el modelo de color que usaremos   
    glutInitWindowSize(w,h)   # Damos el tamaño de la ventana que se mostrará  
    glutInitWindowPosition(300, 50)   # Coordenadas en donde aparecerá la venta en la pantalla  
    wind = glutCreateWindow("Proyecto Final") # Damos un titulo para la ventana
    glutDisplayFunc(showScreen)  # Designamos la función que contiene los elemntos que serán mostrados en la escena 
    glutIdleFunc(showScreen)     
    glutSpecialFunc(processSpecialKeys)
    glutMainLoop()  # Iniciamos el loop principal

if __name__ == "__main__":
    main()