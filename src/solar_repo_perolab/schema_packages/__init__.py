from nomad.config.models.plugins import SchemaPackageEntryPoint


class SolarPackageEntryPoint(SchemaPackageEntryPoint):
    
    def load(self):
        from solar_repo_perolab.schema_packages.schema_package import m_package

        return m_package


solar_package_entry_point = SolarPackageEntryPoint(
    name='Solar Repository Package',
    description='package containing plot and other helper functions for Photovoltaics Characterization.',
)
