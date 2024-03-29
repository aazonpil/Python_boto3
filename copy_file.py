

# Open the source file in write mode
alice_wonderland = ['chap1', 'chap2', 'chap3']
with open('story.txt', 'w') as source_file:
    for chap in alice_wonderland:
        source_file.write(f'Alice in the Wonderland, {chap}\n')

# Function to copy content from the source file to the destination file
def copy_file(story, copy_story):
    with open(story, 'r') as source_file:
        with open(copy_story, 'w') as destination_file:
            # Read the content from the source file
            content = source_file.read()
            # Write the content to the destination file
            destination_file.write(content)

# Call the copy_file function with 'story.txt' as the source and 'new_story.txt' as the destination
copy_file('story.txt', 'copy_story.txt')

print("job sucessfully done")
