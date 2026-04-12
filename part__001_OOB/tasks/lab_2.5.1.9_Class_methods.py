class LuxuryWatch:
    watches_created = 0

    def __init__(self):
        LuxuryWatch.watches_created += 1

    @staticmethod
    def is_engraving_valid(engraving):
        if(len(engraving) > 40): return False
        if(not engraving.isalnum()): return False
        return True

    @classmethod
    def order_with_engraving(cls, engraving):
        if(not cls.is_engraving_valid(engraving)):
            print("engraving: {} is invalid".format(engraving))
        else:
            new_watch = cls()
            new_watch.engraving = engraving
            return new_watch

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.watches_created

print(LuxuryWatch.get_number_of_watches_created())
simple_watch = LuxuryWatch()
print(LuxuryWatch.get_number_of_watches_created())
watch_with_engraving = LuxuryWatch.order_with_engraving("1k2jh41hj13324bk1j2")
print(LuxuryWatch.get_number_of_watches_created())
watch_with_invalid_engraving = LuxuryWatch.order_with_engraving("foo@baz.com")
print(LuxuryWatch.get_number_of_watches_created())


