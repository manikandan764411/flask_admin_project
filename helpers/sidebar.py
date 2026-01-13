from models.user_type_modules import UserTypeModule

def get_sidebar(user_type_id):
    permissions = UserTypeModule.query.filter_by(user_type_id=user_type_id).all()

    menu = []
    for p in permissions:
        menu.append({
            "name": p.module.name,   # ✅ FIXED
            "url": p.module.url,     # ✅ FIXED
            "icon": p.module.icon   # ✅ FIXED
        })

    return menu
