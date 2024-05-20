import xml.sax
import xml.dom.minidom
import matplotlib.pyplot as plt
import datetime

XML_FILE = '/Users/madongge/Downloads/IBI1/IBI1_2023-24/Practical14/go_obo.xml'

def parse_xml_dom(xml_file):
    start_time = datetime.datetime.now()
    dom_tree = xml.dom.minidom.parse(xml_file)
    terms = dom_tree.getElementsByTagName('term')
    
    mf_count = 0
    bp_count = 0
    cc_count = 0
    
    for term in terms:
        namespace = term.getElementsByTagName('namespace')[0].firstChild.data
        if namespace == 'molecular_function':
            mf_count += 1
        elif namespace == 'biological_process':
            bp_count += 1
        elif namespace == 'cellular_component':
            cc_count += 1
    
    end_time = datetime.datetime.now()
    return mf_count, bp_count, cc_count, end_time - start_time

class GoHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.mf_count = 0
        self.bp_count = 0
        self.cc_count = 0
        self.current_namespace = ""
    
    def startElement(self, name, attrs):
        if name == 'namespace':
            self.current_namespace = ""
    
    def characters(self, content):
        self.current_namespace += content
    
    def endElement(self, name):
        if name == 'namespace':
            if self.current_namespace == 'molecular_function':
                self.mf_count += 1
            elif self.current_namespace == 'biological_process':
                self.bp_count += 1
            elif self.current_namespace == 'cellular_component':
                self.cc_count += 1

def parse_xml_sax(xml_file):
    start_time = datetime.datetime.now()
    handler = GoHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    end_time = datetime.datetime.now()
    return handler.mf_count, handler.bp_count, handler.cc_count, end_time - start_time

def main():

    mf_dom, bp_dom, cc_dom, time_dom = parse_xml_dom(XML_FILE)
    
    mf_sax, bp_sax, cc_sax, time_sax = parse_xml_sax(XML_FILE)
    
    print("Results using DOM:")
    print("Molecular Function:", mf_dom)
    print("Biological Process:", bp_dom)
    print("Cellular Component:", cc_dom)
    print("Time taken by DOM:", time_dom)
    print()
    print("Results using SAX:")
    print("Molecular Function:", mf_sax)
    print("Biological Process:", bp_sax)
    print("Cellular Component:", cc_sax)
    print("Time taken by SAX:", time_sax)
    
    labels = ['Molecular Function', 'Biological Process', 'Cellular Component']
    dom_counts = [mf_dom, bp_dom, cc_dom]
    
    x = range(len(labels))
    
    fig_dom, ax_dom = plt.subplots()
    ax_dom.bar(x, dom_counts, width=0.5, label='DOM', color='b')
    
    ax_dom.set_ylabel('Counts')
    ax_dom.set_title('GO Term Counts by Ontology (DOM)')
    ax_dom.set_xticks(x)
    ax_dom.set_xticklabels(labels)
    ax_dom.legend()

    sax_counts = [mf_sax, bp_sax, cc_sax]
    
    fig_sax, ax_sax = plt.subplots()
    ax_sax.bar(x, sax_counts, width=0.5, label='SAX', color='r')
    
    ax_sax.set_ylabel('Counts')
    ax_sax.set_title('GO Term Counts by Ontology (SAX)')
    ax_sax.set_xticks(x)
    ax_sax.set_xticklabels(labels)
    ax_sax.legend()
    
    plt.show()

if __name__ == "__main__":
    main()