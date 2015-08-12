# Problem 1.5: Create method that compress a string using the count of repeated chars
# Example: aabccdddd would become a2b1c2d4 (only compress when the result is smaller than original)

class String
  def get_compressed
    characters = Hash.new
    for i in 0..self.length - 1
      char = self[i]
      next if char == ' '
      if characters[char]
        characters[char] = characters[char] + 1
      else
        characters[char] = 1
      end
    end

    # Normalization #
    result = ''
    characters.each do | key, value|
      result = result + "#{key}#{value}"
    end


    if result.length >= self.length
      self
    else
      result
    end
  end
end