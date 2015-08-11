# Problem 1.4: Replace all white spaces of a string with %20 character

class String
  def transform_spaces!
    self.gsub! ' ', '%20'
  end
end