from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram
from qiskit.providers.ibmq import least_busy
from qiskit import IBMQ

# Anzahl der Qubits
num_qubits = 3  # Ändern Sie dies entsprechend der gewünschten Anzahl von Qubits

# Quantum Circuit erstellen
qc = QuantumCircuit(num_qubits)

# H-Gate auf jedes Qubit anwenden, um Superposition zu erreichen
for qubit in range(num_qubits):
    qc.h(qubit)

# Messungen hinzufügen
qc.measure_all()

# IBM Q Account laden und Backend auswählen
IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q')
backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= num_qubits and 
                                       not x.configuration().simulator and x.status().operational==True))
print("Wir verwenden das Backend: ", backend)

# Transpilieren und Job ausführen
transpiled_qc = transpile(qc, backend, optimization_level=3)
job = backend.run(transpiled_qc)
print(job.job_id())
result = job.result()

# Ergebnisse ausgeben
counts = result.get_counts(qc)
print("\nTotal count for states are:",counts)
plot_histogram(counts)
