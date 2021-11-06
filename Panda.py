from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        

        # Disable the camera trackball controls.
        # self.disableMouse()

        # Load model 
        self.scene = self.loader.loadModel("models/environment")
        # mengembalikan fungsi ke load model
        self.scene.reparentTo(self.render)
        # Memberikan skala pada model
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        # self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load model panda ketika bergerak
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.05, 0.005, 0.05)
        self.pandaActor.reparentTo(self.render)
        # Menambahkan perulangan pada pada model panda (walk4)
        self.pandaActor.loop("walk")

        # Load suara
        mySound = self.loader.loadSfx("musik.ogg")
        # Untuk menyalakan music
        mySound.play()
        # Menambhkan volume
        mySound.setVolume(.5)
        # Untuk membuat perulangan pada musik
        mySound.setLoop(True)
        # Untuk menyalakan musik
        mySound.play()

        # Membuat interval gerakan pada model
        # Untuk membuat model berjalan maju mundur
        posInterval1 = self.pandaActor.posInterval(13,
                                                   Point3(0, -10, 0),
                                                   startPos=Point3(0, 10, 0))
        posInterval2 = self.pandaActor.posInterval(13,
                                                   Point3(0, 10, 0),
                                                   startPos=Point3(0, -10, 0))
        hprInterval1 = self.pandaActor.hprInterval(3,
                                                   Point3(180, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor.hprInterval(3,
                                                   Point3(0, 0, 0),
                                                   startHpr=Point3(180, 0, 0))

        # Membuat dan memainkan urutan yang mengoordinasikan interval.
        self.pandaPace = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace")
        self.pandaPace.loop()

    # Menentukan prosedur untuk menggerakkan kamera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont


app = MyApp()
app.run()
