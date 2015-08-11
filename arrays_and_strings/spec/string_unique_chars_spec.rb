require 'rspec'
require './string_unique_chars.rb'

describe 'Unique characters in string' do
  context "with first implementation"  do
    it 'should detect only unique characters' do
      text = "abcde"
      expect(text.unique_chars_only?).to eq true
    end

    it 'should detect duplicated characters' do
      text = "abacde"
      expect(text.unique_chars_only?).to eq false
    end
  end

  context "with optimized implementation"  do
    it 'should detect only unique characters' do
      text = "zxcvds"
      expect(text.unique_chars_only_optimized?).to eq true
    end

    it 'should detect duplicated characters' do
      text = "oqkslao"
      expect(text.unique_chars_only_optimized?).to eq false
    end
  end
end