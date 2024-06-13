MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You are a helpful geometry problem solver.Let us think step by step and determine what theorems are needed for these geometry problems.'

MATH_CHAT_BETA_PROMPT = '''
We have 30 geometry theorems:
    1: circle_definition,
    2: thales_theorem,
    3: inscribed_angle_theorem,
    4: parallel_lines_theorem,
    5: triangle_anglesum_theorem,
    6: isosceles_triangle_theorem_side,
    7: isosceles_triangle_theorem_angle,
    8: equilateral_polygon_theorem,
    9: pythagoras_theorem,
    10: triangle_center_of_gravity_theorem,
    11: congruent_triangles_proving_theorem,
    12: congruent_triangles_theorem,
    13: law_of_sines,
    14: tangent_secant_theorem,
    15: chord_theorem,
    16: angle_bisector_theorem,
    17: similar_triangle_proving_theorem,
    18: similar_triangle_theorem,
    19: similar_polygon_theorem,
    20: median_line_theorem,
    21: area_equation_theorem,
    22: polygon_anglesum_theorem,
    23: law_of_cosines,
    24: parallelogram_property,
    25: rhombus_property,
    26: rectangle_property,
    27: square_property,
    28: trapezoid_property,
    29: arc_length_formula,
    30: circle_area_formula,
    31: auxiliary_line_formula.

Please read the following geometry question and select the correct theorems(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31). 

After selecting theorems, please re-examine the problem with the chosen theorems to ensure it is consistent and correct. If you find any inconsistencies or reconsider your reasoning, feel free to revise your answer.

After your self-consistency, **provide the answer theorems in the format: "Theorems: [1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31]". Do not put extra information except for your option after 'Theorems:' ** 


For example:
Question:
    PointLiesOnLine(K, Line(G, J)), PointLiesOnLine(K, Line(F,H)), Equals(LengthOf(Line(F,K)),3x-1), Equals(LengthOf(Line(K,G)),4y+3), Equals(LengthOf(Line(J,K)),6y-2), Equals(LengthOf(Line(K,H)),2x+3), Parallelogram(F,G,H,J), Find(x).
    
Because Parallel(Line(F,G)),LengthOf(Line(F,K)), we can apply theorem 4, which states that Equals(MeasureOf(Angle(G,F,K)),Angle(J,H,K))),Equals(MeasureOf(Angle(F,G,K)),Angle(H,J,K)));
Because Equals(LengthOf(Line(F,G)),LengthOf(Line(F,K))),Equals(MeasureOf(Angle(G,F,K)),Angle(J,H,K))),Equals(MeasureOf(Angle(F,G,K)),Angle(H,J,K))), we can apply theorem 11, which states that Congruent(Triangle(F,G,K),Triangle(H,J,K));
Because Congruent(Triangle(F,G,K),Triangle(H,J,K)), we can apply theorem 12, which states that Equals(LengthOf(Line(F,K)),LengthOf(Line(K,H)));
we can apply 3x-1=2x+3, x=4, Thus, you should answer: "Theorems: [4,11,12]"

Now, let's find theorems of the following question with this approach.


'''