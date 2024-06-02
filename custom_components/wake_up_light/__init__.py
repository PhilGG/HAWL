import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    _LOGGER.info("Setting up Wake Up Light integration.")
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    _LOGGER.info(f"Setting up Wake Up Light entry: {entry.data}")
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    _LOGGER.info(f"Unloading Wake Up Light entry: {entry.entry_id}")
    hass.data[DOMAIN].pop(entry.entry_id)
    return True