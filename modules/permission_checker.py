"""
نظام فحص الصلاحيات المركزي
"""

from datetime import datetime

class PermissionChecker:
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def check_command_permission(self, user, command: str) -> dict:
        """فحص صلاحيات الأمر"""
        username = user.username
        user_id = user.id

        is_owner = self.user_manager.is_owner(username)
        is_moderator = self.user_manager.is_moderator(username)
        user_type = self.user_manager.get_user_type(username, user_id)

        # أوامر المالك فقط
        owner_commands = [
            "اضافة_مشرف @", "ازالة_مشرف @", "احذف مكان", "promote ", "demote ",
            "اضافة_vip @", "ازالة_vip @", "إضافة_vip @", "إزالة_vip @", "/نقل "
        ]

        # أوامر المشرفين
        moderator_commands = [
            "حفظ", "اذهب", "الاماكن", "عدد الاماكن", "اسحبهم", "جيب @",
            "بدل", "bot_dance", "رقص البوت", "تغيير", "ريأكشن",
            "المشرفين", "فحص @", "فحصني", "احصائيات_الغرفة",
            "قائمة_المشرفين", "ثبت @", "الغ ثبت @", "إلغاء_التثبيت @",
            "سجن @", "المثبتين", "ايقاف @", "رقص_الكل", "ايقاف_الكل",
            "غرفة", "حالة_الغرفة", "فحص_صلاحيات @", "مزامنة_الصلاحيات",
            "قائمة_vip", "vip_list", "الـvip"
        ]

        # أوامر VIP
        vip_commands = [
            "وديني @", "اعكس @"
        ]

        # فحص نوع الأمر
        requires_owner = any(command.startswith(cmd) for cmd in owner_commands)
        requires_moderator = any(command.startswith(cmd) or command == cmd for cmd in moderator_commands)
        requires_vip = any(command.startswith(cmd) for cmd in vip_commands)

        # النتيجة
        result = {
            "allowed": True,
            "user_type": user_type,
            "is_owner": is_owner,
            "is_moderator": is_moderator,
            "is_vip": self.user_manager.is_vip(user_id) if hasattr(self.user_manager, 'is_vip') else False,
            "message": None
        }

        if requires_owner and not is_owner:
            result["allowed"] = False
            result["message"] = f"❌ المعذرة يا {username}، الأمر ده للريس بس! إنت مش صاحب البوت"
        elif requires_moderator and not is_moderator and not is_owner:
            result["allowed"] = False
            result["message"] = f"❌ آسف يا {username}، الأمر ده للمشرفين بس!\n👤 إنت: {user_type}\n💡 كلم المشرفين علشان يدوك الصلاحيات"
        elif requires_vip and not result["is_vip"] and not is_moderator and not is_owner:
            result["allowed"] = False
            result["message"] = f"❌ آسف يا {username}، الأمر ده للـ VIP بس!\n👤 إنت: {user_type}\n💡 كلم المشرفين علشان يدوك صلاحيات VIP"

        return result

    def get_user_permissions_summary(self, username: str, user_id: str = None) -> str:
        """ملخص صلاحيات المستخدم"""
        is_owner = self.user_manager.is_owner(username)
        is_moderator = self.user_manager.is_moderator(username)
        is_vip = self.user_manager.is_vip(user_id) if hasattr(self.user_manager, 'is_vip') and user_id else False
        user_type = self.user_manager.get_user_type(username, user_id)
        emoji = self.user_manager.get_user_emoji(username)

        summary = f"{emoji} صلاحيات {username}:\n"
        summary += f"🏷️ النوع: {user_type}\n"

        if is_owner:
            summary += "✅ يمكنه استخدام جميع الأوامر\n"
            summary += "✅ إدارة المشرفين والـ VIP\n"
            summary += "✅ إدارة الأماكن"
        elif is_moderator:
            summary += "✅ أوامر المشرفين\n"
            summary += "✅ إدارة المستخدمين\n"
            summary += "❌ لا يمكنه إدارة المشرفين أو VIP"
        elif is_vip:
            summary += "✅ أوامر VIP الخاصة\n"
            summary += "✅ أوامر النقل المتقدمة\n"
            summary += "❌ لا يمكنه استخدام أوامر المشرفين"
        else:
            summary += "✅ الأوامر العامة فقط\n"
            summary += "❌ لا يمكنه استخدام أوامر المشرفين أو VIP"

        return summary