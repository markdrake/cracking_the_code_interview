# Problem: Decide if one text is an anagram of another given.
# The strings will be treated case sensitive so whitespace would make them different and Dog and God are not anagrams.

class String
  def is_anagram_of?(other)
    return false unless other.is_a? String      # No string then we can't compare
    return false if self.length != other.length # If the length is different there's no point in comparing

    self == other.reverse # Compare if both strings are equal when put in order
  end
end