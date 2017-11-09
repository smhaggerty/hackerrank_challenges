# Your code here
def convert_temp(temp, input_scale: , output_scale: 'Celsius')
    case input_scale.downcase
    when 'celsius'
        return output_scale == 'fahrenheit' ? temp * 1.8 + 32 : temp + 273.15 
    when 'fahrenheit'
        return output_scale == 'celsius' ? (temp - 32) / 1.8 : ((temp - 32) / 1.8) + 273.15
    when 'kelvin'
        return output_scale == 'fahrenheit' ? (temp - 273.15) * 1.8 + 32: temp - 273.15
    end
end