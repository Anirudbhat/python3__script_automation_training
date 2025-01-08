import platform

# print(dir(platform))

# print(help(platform))

'''
Various functions from PLATFORM module
'''

print(f'This is running on {platform.system()} os')
print(f'Python version is {platform.python_version()}')
print(platform.python_version_tuple())
print(platform.machine())
print(platform.release())
print(platform.platform())
print(platform.architecture())
print(platform.processor())
print(platform.node())
print(platform.uname())
