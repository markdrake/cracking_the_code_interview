require 'rspec'
require './replace_spaces'

describe 'Replace spaces' do

  it 'should replace spaces' do
    text = 'This is a text  '
    expected = 'This%20is%20a%20text%20%20'

    expect(text.transform_spaces!).to eq expected
  end
end