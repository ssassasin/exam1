''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.)

*   Create a VE and name it quiz_ve. Install the 3rd party libraries- wordcloud and imageio.
    Make sure your VE is NOT part of your repository. Make sure your .gitignore
    IS part of your repo. The code will produce a heart-shaped wordcloud of the most
    frequently appearing words in the text of Romeo and Juliet.

*   Create a dictionary of each student where the student FULL NAME (proper casing) is the key
    and the GPA is the value. 

*   print out the dictionary

*   print out the corresponding GPA for student - Luke Brazzi

*   push your repo to GitHub. Only your VE should not be in your repo. Everything else should be
    pushed. Submit your Github repo URL in the response field of the quiz.

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv
with open ('students.csv', 'r') as infile, open ('processedStudents.csv', 'w', newline='') as outfile:
    reader= csv.reader(infile)
    writer= csv.writer(outfile)

    header= next(reader)
    writer.writerow(header)

    student_lookup= {}

    for row in reader:
        try:
            first_name= row[2] 
            last_name= row[3] 
            gpa= float(row[8])

        except (IndexError, ValueError):
            print(f"Skipping row due to an error: {row}")
            continue

        full_name= f"{first_name}, {last_name}".title()
        student_lookup[full_name]= gpa

        if gpa< 3.0:
            writer.writerow(row)
            print(f"{full_name} has a GPA of {gpa} below 3.0")

print(student_lookup)



#display the wordcloud
from pathlib import Path
from wordcloud import WordCloud
import imageio.v2 as imageio
import matplotlib.pyplot as plt


text = Path("RomeoAndJuliet.txt").read_text()
mask_image = imageio.imread("mask_heart.png")
wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")
wordcloud = wordcloud.generate(text)
wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()







