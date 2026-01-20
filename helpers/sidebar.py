from models.user_type_modules import UserTypeModule
from models.module import Module

def get_sidebar(user_type_id):
    permissions = (
        UserTypeModule.query
        .join(Module)
        .filter(
            UserTypeModule.user_type_id == user_type_id,
            Module.is_active == True
        )
        .all()
    )

    sidebar = {}

    # 1️⃣ Create parent modules
    for p in permissions:
        module = p.module

        if module.parent_id is None:
            sidebar[module.id] = {
                "name": module.name,
                "url": module.url,
                "icon": module.icon,
                "children": []
            }

    # 2️⃣ Attach submodules
    for p in permissions:
        module = p.module

        if module.parent_id and module.parent_id in sidebar:
            sidebar[module.parent_id]["children"].append({
                "name": module.name,
                "url": module.url,
                "icon": module.icon
            })

    return sidebar.values()
