
class NseScript:
    def __init__(self, name=None, short_description=None, full_description=None, sample_usages=None, categories=None, reference_links=None):
        self.name = name
        self.short_description = short_description
        self.full_description = full_description
        self.sample_usages = sample_usages
        self.categories = categories
        self.reference_links = reference_links

    def __str__(self):
        return """NseScript(
        name = {0}
        description = {1},
        categories = {2},
        sample_usages = {3}
)""".format(self.name, self.short_description, self.categories, self.sample_usages)