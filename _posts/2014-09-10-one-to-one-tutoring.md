---
layout: post
title: One-to-One Tutoring
author: Martin Thoma
date: 2014-09-10 10:03
categories:
- My bits and bytes
tags:
- KIT
featured_image: logos/kit.png
---

I have heard that the famous high quality universities in England have
One-to-One tutoring. That means one tutor helps one student only. That must
be incredible effective for learning. From my experience as a tutor and as a
"coach" (Nachhilfelehrer) I know that there is a huge difference in One-to-One
tutoring compared to One to Many tutoring. If you only have one student, you
can focus on the needs of this single student. And I guess that the student
will also be encouraged a bit more to participate. If you only have one student,
the student will not sleep while you teach him. He has to stay focused, because
you will notice when he doesn't.

So One-to-One tutoring is something we want to get.

## The problem of One-to-One tutoring
But it is expensive, if it would be done like tutoring is currently done. In
fact I think it would be impossible, because you would not find that many
tutors. However, I think there is another way to motivate students that have
already passed the exam to be a tutor for another student:

## The way to get One-to-One tutoring
Give One-to-One tutors the possibility to try the exam again.

I could imagine it to work like this: A student passes the exam, but he does
not have the grade he wants. As he has already passed the exam, he will not be
allowed to simply do it again. So he has to search a student who hasn't already
passed the exam and help this student to prepare for the exam. Now we have to
check if the One-to-One tutor really helped the new student. I could imagine
two ways that could also be combined.

### One-to-One tutoring: Way 1
The One-to-One tutor has to help the new student with the excercises. So the
One-to-Many tutor gets the information which excercises were done by the
One-to-One tutor and the new student. So in contrast to now, not only one
student would make an excercise, but two. In order to make sure that there is
an improvement, one could increase the necessary number of points for the
One-to-One tutor to a threshold of $\theta_1$ (or both, the new student and the One-to-One tutor). $\theta_1$ should denote how much more points the tutor needs (in
percent of the points the students need) to get the possibility to re-do the
exam.

So $\theta_1 = 0$ would mean that the tutor does only need a student how
gets the minimum number of points to pass the exam.

$\theta_1 = 1$ would mean that the tutor needs his students to get double the
number of points in the excercises than what he would need to be allowed to
participate in the exam.

This means $\theta_1 \in [0, 1]$.

$\theta_1$ should not be zero, because that
would mean that 1-to-1 tutors could choose their students right before the exam.
But I want them to choose the student at the beginning of the semester. And
$\theta_1$ may not be too high. The higher it gets, the more difficult and time
intensive it gets for the student and the tutor. I think the time right before
an exam is the time where students learn most. If a student doesn't achive
the $\theta_1$ threshold, then the tutor will not have any incent to help the
student to prepare for the exam except for money or friendship.

### One-to-One tutoring: Way 2
The other possibility would be to enforce a minimum grade for the tutored
student. So the One-to-One tutor cannot participate in the same exam as his
student. But in the one after that. And he can only participate in that exam
if his student got a minimum grade $\theta_2$, e.g. 2.3 or better.

$\theta_2 = 5$ would mean that the student only has to participate in the exam
(At KIT every student gets at least a grade of 5. The best grade is 1.0.).

$\theta_2 = 1$ would mean that the student has to pass with the best grade so
that the tutor is allowed to participate in the exam.

Alternatively one could make that dependant on the number of students who got
the grade. So $\theta_2 = 10\%$ would mean that you choose the grade threshold
in a way that makes sure that at least 10% of all students pass that
requirement.

This means $\theta_2 \in [1, 5]$ or $\theta_2 \in (0\%, 100\%]$.

$\theta_2$ should not be too bad (near 5), because then it will be too easy
for many students to get another try for the exam. That would also not help the
students, because the tutor would not have an incent that is strong enough to
increase the abilities of his student. However, if $\theta_2$ gets too low
(near 1.0) then most students will not try to be a tutor because it is too
difficult to get a student to achieve that good results.

## How to speak about it

I would like to call this model MOOT (Martins One-to-One Tutoring model).
It is parameterized with two variables, $\theta_1$ and $\theta_2$.

I think $MOOT(\theta_1=1.2, \theta_2=25\%)$ would be a good possibility to
encourage students to help other students effectively. $\theta_1$ is low enough
to make it fairly easy for somebody who already passed the exam to "lift" a
student to pass the requirement.

So I guess $MOOT(0.2, 25\%)$ would be a good choice.

## Conclusion
The two ways I proposed would in general lead to better students, remove stress
from students because a single bad exam would not be that bad any more and
very likely lead to better students. Students would be better on the paper
(because the tutor should only be able to improve himself by the new exam and
also his student should be able to achive better results in the exam) and in
the real world. Students would get an incentive to repeat what they did not
understand before. They would get an incentive to help other students. For free.
And it would not be that much more work for the university. I think it is easier
to correct exams of good students and only a few would really take this
possibility as it is really time intensive for the One-to-One tutor. But for
some exams and some students that might be worth the effort.

What do you think about it? Do you think we could introduce that model at KIT?
Who could propose it? To whom should it be proposed?