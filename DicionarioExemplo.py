usuarios = {}
print(usuarios)

usuarios = {
    "chaves": ["Chaves do 8", "24/12/2017", "Recep_01"],
    "quico" : {"Quico das flores", "20/12/2017", "Raiox_03"}
}
print(usuarios)

usuarios["florinda"] = ["Dona Florinda", "24/12/17", "Raiox_01"]
print(usuarios)

print(usuarios.get("quico"))
for i in (usuarios):
    if i == "florinda":
        pass
    else:
        print(i)