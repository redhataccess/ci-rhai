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
  f.write('TIME=' + time)
