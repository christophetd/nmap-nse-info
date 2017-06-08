from NseParsingException import NseParsingException
from nseinfo.NseScript import NseScript
import nltk
from nltk import tokenize
import re

NSE_EXTENSION = '.nse'

class NseScriptParser:
    """
    Builds a NseScript object from the contents of a NSE file
    """
    def parse(self, file_name, nse_file_contents):
        try:
            tokenize.sent_tokenize('')
        except LookupError as e:
            nltk.download('punkt')

        if nse_file_contents is None or len(nse_file_contents) == 0:
            raise NseParsingException("Empty NSE script contents")

        # Remove extension if needed
        if file_name.endswith(NSE_EXTENSION):
            file_name = file_name[:-len(NSE_EXTENSION)]


        full_description = self.__parse_full_description(nse_file_contents)
        short_description = self.__get_short_description(full_description)
        categories = self.__parse_categories(nse_file_contents)
        sample_usages = self.__parse_sample_usages(nse_file_contents)

        return NseScript(
            full_description = full_description,
            short_description = short_description,
            categories = categories,
            sample_usages = sample_usages,
            name = file_name
        )

    def __parse_full_description(self, nse_file_contents):
        description_regex = r'.*?description\s*=\s*\[\[(.*?)\]\]'
        full_description_match = re.match(description_regex, nse_file_contents, re.S|re.I)

        if not full_description_match or len(full_description_match.groups()) < 1:
            # Attempt the alternative format where the description is on a single line
            description_regex = r'.*?description\s*=\s*"(.*?)"'
            full_description_match = re.match(description_regex, nse_file_contents, re.S | re.I)
            if not full_description_match or len(full_description_match.groups()) < 1:
                raise NseParsingException("Unable to parse description from NSE script content")

        full_description_raw = full_description_match.groups(1)[0]

        return self.__strip_html_tags(full_description_raw.strip())

    def __get_short_description(self, full_description):
        sentences = tokenize.sent_tokenize(full_description)
        return sentences[0].replace('\n', ' ')

    def __parse_categories(self, nse_file_contents):
        categories_regex = r'.*?categories\s*=\s*\{(.*?)\}'
        categories_match = re.match(categories_regex, nse_file_contents, re.S|re.I)

        if not categories_match or len(categories_match.groups()) < 1:
            raise NseParsingException("Unable to parse categories from NSE script content")

        categories_raw = re.sub(r'[^a-zA-Z,]', '', categories_match.groups(1)[0])
        categories = categories_raw.split(',')

        return categories

    def __parse_sample_usages(self, nse_file_contents):
        sample_usages_regex = r'.*?@usage(.*)@output'
        sample_usages_match = re.match(sample_usages_regex, nse_file_contents, re.S|re.I)

        if not sample_usages_match or len(sample_usages_match.groups()) < 1:
            return []

        sample_usages_raw = sample_usages_match.groups(1)[0].lstrip().replace("-- ", "").split("\n")[:-1]
        return [ el for el in sample_usages_raw if re.match("^\s*nmap.+", el, re.I) ]

    def __strip_html_tags(self, str):
        return re.sub('<[^<]+?>', '', str)