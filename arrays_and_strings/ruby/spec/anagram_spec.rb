require 'rspec'
require './anagram'

describe 'Anagram analyzer funciton' do
  it 'should detect a valid anagram' do
    text = 'dog'
    other_text = 'god'

    expect(text.is_anagram_of? other_text).to be true
  end

  it 'should detect an invalid anagram' do
    text = 'mark'
    other_text = 'john'

    expect(text.is_anagram_of? other_text).to be false

  end
end
