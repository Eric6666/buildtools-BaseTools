import Section
import subprocess
from Ffs import Ffs
class GuidSection(Section.Section) :
    
    def __init__(self):
        self.Alignment = None
        self.NameGuid = None
        self.SectionList = []
        
    def GenSection(self, OutputPath, ModuleName):
        #
        # Generate all section
        #
        SectFile = ''
        for Sect in self.SectionList:
            SectFile = SectFile + \
                       '  '     + \
                       Sect.GenSection(OutputPath, ModuleName)

        OutputFile = OutputPath + \
                     ModuleName + \
                     Ffs.SectionSuffix['GUIDED']
                     
        GenSectionCmd = 'GenSection -o '                  + \
                         OutputFile                       + \
                         ' -s '                           + \
                         Section.Section.SectionType[self.SectionType] + \
                         SectFile
        #
        # Call GenSection
        #
        print GenSectionCmd
        subprocess.Popen (GenSectionCmd).communicate()
        
        #
        # Use external tool process the Output
        #
        InputFile = OutputFile
        TempFile = OutputPath + \
                   ModuleName + \
                   '.tmp'
                   
        ExternalToolCmd = Section.Section.ToolGuild[self.NameGuid] + \
                          ' -o '                                   + \
                          TempFile                                 + \
                          ' '                                      + \
                          InputFile

        #
        # Call external tool
        #
        print ExternalToolCmd
        subprocess.Popen (ExternalToolCmd).communicate()
        #
        # Call Gensection Add Secntion Header
        #
        GenSectionCmd = 'GenSection -o '                        + \
                         OutputFile                             + \
                         ' -s '                                 + \
                         Section.Section.SectionType['GUIDED']  + \
                         ' '                                    + \
                         TempFile
                        
        print GenSectionCmd
        subprocess.Popen(GenSectionCmd).communicate()
        return OutputFile
