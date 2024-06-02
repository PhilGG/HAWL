import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
import logging
from .const import DOMAIN, CONF_DURATION, DEFAULT_DURATION

_LOGGER = logging.getLogger(__name__)

class WakeUpLightConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        _LOGGER.info("Starting user step in config flow.")
        if user_input is not None:
            try:
                _LOGGER.info(f"User input received: {user_input}")
                return self.async_create_entry(title="Wake Up Light", data=user_input)
            except Exception as e:
                _LOGGER.error(f"Error creating entry: {e}")
                errors["base"] = "cannot_create_entry"

        schema = vol.Schema({
            vol.Required("example_field"): str,
            vol.Optional(CONF_DURATION, default=DEFAULT_DURATION): vol.Coerce(int),
        })

        return self.async_show_form(
            step_id="user", data_schema=schema, errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return WakeUpLightOptionsFlow(config_entry)

class WakeUpLightOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            _LOGGER.info(f"Options flow user input received: {user_input}")
            return self.async_create_entry(title="", data=user_input)

        schema = vol.Schema({
            vol.Required("example_field", default=self.config_entry.options.get("example_field", "")): str,
            vol.Optional(CONF_DURATION, default=DEFAULT_DURATION): vol.Coerce(int),
        })

        return self.async_show_form(
            step_id="init", data_schema=schema
        )
