# config for TipoSeguro using EAV

from eav.registry import EavConfig

class TipoSeguroEavConfig(EavConfig):
    manager_attr = 'seguroObjects'

class CoberturaEavConfig(EavConfig):
    manager_attr = 'coberturaObjects'
