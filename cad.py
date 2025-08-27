import cadquery as cq
import math

# ==========================
# PARAMETER PEGAS
# ==========================
d_wire = 33.5       # Diameter kawat (mm)
D_mean = 211        # Diameter rata-rata (mm)
n_turns = 8
pitch = 68          # mm
n_points_per_turn = 50  # jumlah titik per lilitan untuk smoothness

R_mean = D_mean / 2
height = pitch * (n_turns - 1)

# ==========================
# BIKIN HELIX POINTS
# ==========================
points = []
for i in range(n_turns * n_points_per_turn + 1):
    t = i / n_points_per_turn * 2 * math.pi
    x = R_mean * math.cos(t)
    y = R_mean * math.sin(t)
    z = pitch * t / (2*math.pi)
    points.append((x, y, z))

# ==========================
# BUAT HELIX SWEEP (PIPE)
# ==========================
helix_wire = cq.Workplane("XY").spline(points)
spring = cq.Workplane("XY").workplane().circle(d_wire/2).sweep(helix_wire)

# ==========================
# EXPORT STEP
# ==========================
output_file = "spring_2000kg_codespace_cq.step"
spring.val().exportStep(output_file)
print(f"✅ STEP berhasil dibuat: {output_file}")

# ==========================
# PETUNJUK SIMSCALE
# ==========================
print("""
Panduan SimScale:

1. Import file STEP: 'spring_2000kg_codespace_cq.step'
2. Assign Material: Steel
   - Density: 8000 kg/m³
   - Young's Modulus: 207 GPa
   - Poisson's Ratio: 0.33
   - Yield Strength: 800 MPa
   - Ultimate Tensile Strength: 924 MPa
3. Boundary Conditions:
   - Fixed support di salah satu ujung heliks
   - Force = 19613 N (2000 kg × 9.81) di ujung yang berlawanan
4. Mesh: gunakan Fine Mesh / Hex-Dominant
5. Run Simulation: Static Structural
""")
