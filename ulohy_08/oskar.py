import class_closure
import class_fabrics
import class_interfacings
import class_straps
import class_plastic_components


product = "batoh Oskar"
magnet = class_closure.Closure(product)
price_closure = round(magnet.closure_price(), 2)

lining = class_fabrics.Fabrics("podšívka", "plátno")
price_lining = round(lining.fabric_price(), 2)

outer = class_fabrics.Fabrics("vnější", "kočárkovina")
price_outer = round(outer.fabric_price(), 2)

ronolin = class_interfacings.Interfacings("ronolin")
price_interfacing = round(ronolin.interfacing_price(), 2)

strap = class_straps.Straps("bavlna")
price_strap = round(strap.strap_price(), 2)

component = class_plastic_components.Plastic_components("žebříček")
price_component = round(component.component_price(), 2)

price = round(price_closure + price_lining + price_outer + price_interfacing +
              price_strap + price_component, 2)

print(f"\nCena materiálu na zapínání je {price_closure} Kč.")
print(f"Část: {lining.part}, materiál: {lining.fabric_type}, cena: {price_lining} Kč.")
print(f"Část: {outer.part}, materiál: {outer.fabric_type}, cena: {price_outer} Kč.")
print(f"Cena výztuhy je {price_interfacing} Kč.")
print(f"Cena popruhu z materiálu {strap.material} je {price_strap} Kč.")
print(f"Cena {component.type} je {price_component} Kč.")
print(f"\nCena materiálu na {product} je {price} Kč.")
