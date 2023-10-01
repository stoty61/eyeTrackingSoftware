from warning_display import *


warning_1 = WarningDisplay("Visual")
warning_1.warning_init("icon.png", "UDP", "localhost", 20001, 1024)
warning_1.warning()
warning_1.root.after(1, warning_1.warning)
warning_1.root.mainloop()