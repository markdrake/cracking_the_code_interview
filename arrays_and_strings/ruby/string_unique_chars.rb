# Problem : Create a function that determines if the string contains only unique chars.

class String
  # First implementation, slower but working
  def unique_chars_only?
    max_chars = 256
    return false if self.length > max_chars

    for outer_position in 0..self.length - 1 
      for inner_position in 0..self.length - 1 
        next if outer_position == inner_position 
        return false if (self[outer_position] == self[inner_position])
      end
    end

    true
  end

  def unique_chars_only_optimized?  # complexity O (n), space O(1)
    max_chars = 256
    return false if self.length > max_chars

    char_set = Array.new (max_chars)
    for i in 0..self.length - 1
      val = self[i].ord
      return false if char_set[val]
      char_set[val] = true
    end

    true
  end
end
