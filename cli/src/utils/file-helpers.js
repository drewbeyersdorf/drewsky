import fs from 'fs-extra';
import path from 'path';

const DREWSKY_DIR = '.drewsky';
const METRICS_FILE = path.join(DREWSKY_DIR, 'metrics.json');
const CONFIG_FILE = path.join(DREWSKY_DIR, 'config.json');

export async function updateMetrics(updates) {
  try {
    const metrics = await fs.readJSON(METRICS_FILE);

    // Increment counters
    for (const [key, value] of Object.entries(updates)) {
      if (typeof value === 'number') {
        metrics[key] = (metrics[key] || 0) + value;
      } else if (typeof value === 'object') {
        metrics[key] = { ...metrics[key], ...value };
      }
    }

    // Update timestamp
    metrics.lastUpdated = new Date().toISOString();

    await fs.writeJSON(METRICS_FILE, metrics, { spaces: 2 });
    return metrics;
  } catch (error) {
    console.warn('Warning: Could not update metrics:', error.message);
    return null;
  }
}

export async function getMetrics() {
  try {
    return await fs.readJSON(METRICS_FILE);
  } catch (error) {
    return null;
  }
}

export async function getConfig() {
  try {
    return await fs.readJSON(CONFIG_FILE);
  } catch (error) {
    return null;
  }
}

export async function fileExists(filePath) {
  try {
    await fs.access(filePath);
    return true;
  } catch {
    return false;
  }
}

export async function readWorkflowFiles() {
  const files = {
    research: await fileExists('.research.md'),
    plan: await fileExists('.plan.md'),
    completion: await fileExists('.completion-snapshot.md')
  };

  return files;
}
