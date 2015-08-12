require 'rspec'
require './string_compression'

describe 'String compression' do

  it 'should compress' do
    text     = 'this is a string that requires being compressed'
    expected = 't4h2i5s6a2r4n2g2e5q1u1b1c1o1m1p1d1'

    expect(text.get_compressed).to eq expected
  end

  it 'should not compress when compressed version is same length or bigger than original one' do
    original = 'abcdefg'

    expect(original.get_compressed).to eq original
  end
end