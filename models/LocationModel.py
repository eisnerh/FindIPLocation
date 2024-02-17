class Rootobject:
    def __init__(self):
        self.ip = ""
        self.success = False
        self.type = ""
        self.continent = ""
        self.continent_code = ""
        self.country = ""
        self.country_code = ""
        self.region = ""
        self.region_code = ""
        self.city = ""
        self.latitude = 0.0
        self.longitude = 0.0
        self.is_eu = False
        self.postal = ""
        self.calling_code = ""
        self.capital = ""
        self.borders = ""
        self.flag = Flag()
        self.connection = Connection()
        self.timezone = Timezone()


class Flag:
    def __init__(self):
        self.img = ""
        self.emoji = ""
        self.emoji_unicode = ""


class Connection:
    def __init__(self):
        self.asn = 0
        self.org = ""
        self.isp = ""
        self.domain = ""


class Timezone:
    def __init__(self):
        self.id = ""
        self.abbr = ""
        self.is_dst = False
        self.offset = 0
        self.utc = ""
        self.current_time = ""


# Ejemplo de uso:
# Crear una instancia de Rootobject
root_obj = Rootobject()

# Acceder a los atributos
print(root_obj.ip)
print(root_obj.success)
print(root_obj.flag.emoji)
print(root_obj.timezone.current_time)
