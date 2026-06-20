class base:
    def show(self):
        print("Show from base class")
class derived(base):
    def show(self):
        print("show from derived class")
class subderived(derived):
    def show(self):
        super().show()
        print("Show from subderived class")
da= subderived()
da.show()
