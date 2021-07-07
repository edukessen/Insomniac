from insomniac import save_crash
from insomniac.device_facade import DeviceFacade

is_old = False
device_id = None
app_id = "com.instagram.android"

device = DeviceFacade(is_old, device_id, app_id, None)
save_crash(device)
