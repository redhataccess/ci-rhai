import xml.etree.ElementTree as ET

tree = ET.parse('./foreman-results.xml')
root = tree.getroot()

tests = root.attrib.get('tests')
errors = root.attrib.get('errors')
failures = root.attrib.get('failures')
skips = root.attrib.get('skips')
time = root.attrib.get('time')
tests_passed = int(tests) - int(failures)

with open('env.properties','w') as f:
  f.write('ERRORS=' + errors+ '\n')
  f.write('FAILURES=' + failures + '\n')
  f.write('TESTS=' + tests + '\n')
  f.write('SKIPS=' + skips + '\n')
  f.write('TESTS_PASSED=' + str(tests_passed) + '\n')
  f.write('TIME=' + time + "\n")

tests_array=[]
for child in root:
  test_attribute = child.attrib
  for f in child:
    if f.tag == "failure":
      failure_attribute = f.attrib
      final_tests = dict(test_attribute.items() + failure_attribute.items())
      tests_array.append(final_tests)
      break
    else:
      tests_array.append(test_attribute)
print tests_array

for i in range(len(tests_array)):
  with open('env.properties', 'a') as f:
    f.write("TEST_CASE" + str(i) + "=" + str(tests_array[i]) + "\n")



