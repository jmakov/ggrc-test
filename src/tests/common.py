class string_utils():
    """
    Common string utils.
    """
    def get_string_in_brackets(self, instr):
        """
        Return string between brackets ()
        """
        return instr[instr.find("(")+1:instr.find(")")]

    def get_num_in_brackets(self, instr):
        """
        Get number from string between brackets
        """
        return int(self.get_string_in_brackets(instr))
