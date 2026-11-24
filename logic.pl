% ==========================================
% KNOWLEDGE BASE FOR UNIVERSITY ORIENTATION
% ==========================================

% --- FACTS (Student Profiles) ---
% Format: student(ID, Name, Math, Prog, Interest)
student('S1', 'Alice', 18, 16, 'AI').
student('S4', 'David', 8, 18, 'Software').
student('S9', 'Ivan', 16, 0, 'Cyber'). % 0 means missing/failed here for simplicity

% --- CLASSICAL LOGIC RULES (Strict) ---
% AI needs Math >= 15 AND Prog >= 14
is_accessible_ai(M, P) :- M >= 15, P >= 14.

% Software needs Prog >= 12
is_accessible_software(P) :- P >= 12.

% Cyber needs Math >= 12 AND Interest == 'Cyber'
is_accessible_cyber(M, I) :- M >= 12, I == 'Cyber'.

% --- DEFAULT LOGIC RULES (Exceptions) ---
% By default, if they like AI, they are suited.
% Unless (Exception) their Math is < 10.
suited_ai_default(I, M) :- I == 'AI', M >= 10.

% By default, if they like Software, they are suited.
% Unless Programming is < 8.
suited_software_default(I, P) :- I == 'Software', P >= 8.

% --- MASTER RULE (Forward Chaining style) ---
% A student is recommended for a major if they pass the strict rule AND the default rule.
recommend(ID, Major) :-
    student(ID, _, M, P, I),
    (
        (Major == 'AI', is_accessible_ai(M, P), suited_ai_default(I, M)) ;
        (Major == 'Software', is_accessible_software(P), suited_software_default(I, P)) ;
        (Major == 'Cyber', is_accessible_cyber(M, I))
    ).