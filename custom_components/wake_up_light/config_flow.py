import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv
from .const import DOMAIN, CONF_LIGHTS, CONF_DURATION, DEFAULT_DURATION

class WakeUpLightConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Wake Up Light", data=user_input)

        schema = vol.Schema({
            vol.Required(CONF_LIGHTS): vol.All(cv.ensure_list, [cv.entity_id]),
            vol.Optional(CONF_DURATION, default=DEFAULT_DURATION): cv.positive_int,
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
            return self.async_create_entry(title="", data=user_input)

        schema = vol.Schema({
            vol.Required(CONF_LIGHTS, default=self.config_entry.options.get(CONF_LIGHTS, [])): vol.All(cv.ensure_list, [cv.entity_id]),
            vol.Optional(CONF_DURATION, default=self.config_entry.options.get(CONF_DURATION, DEFAULT_DURATION)): cv.positive_int,
        })

        return self.async_show_form(
            step_id="init", data_schema=schema
        )
